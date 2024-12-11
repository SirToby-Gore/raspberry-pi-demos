import { createClient } from "@supabase/supabase-js";
import Chart from "chart.js/auto";
let interval;
let myChart;
const timer = document.getElementById('timer');
const timerWrap = document.getElementById('timer-wrap');
const timerInital = 60;
let remainingTime = timerInital;

const supabase = createClient(import.meta.env.VITE_SUPABASE_URL, import.meta.env.VITE_SUPABASE_ANON_KEY);

async function fetchData() {
  const { data, error } = await supabase
    .from('readings')
    .select('temperature, pressure, humidity, created_at')
    .order('created_at', { ascending: true });

  if (error) {
    console.error("Error fetching data:", error);
    return [];
  }

  return data;
}


function formatTimestamp(timestamp) {
  const date = new Date(timestamp);

  const year = date.getUTCFullYear();
  const month = String(date.getUTCMonth() + 1).padStart(2, '0'); // months are 0 indexed for some dumb reason
  const day = String(date.getUTCDate()).padStart(2, '0');
  const hours = String(date.getUTCHours()).padStart(2, '0');
  const minutes = String(date.getUTCMinutes()).padStart(2, '0');

  return `${year}-${month}-${day} ${hours}:${minutes}`;
}

function updateNotice(timestamp) {
  const notice = document.getElementById("data-notice");
  const lastReading = new Date(timestamp);
  const now = new Date();
  const diffInSeconds = (now - lastReading) / 1000;

  if (diffInSeconds > 60) {
    notice.textContent = `Data is not being collected. Last reading ${formatTimestamp(lastReading)}.`;
    notice.style.color = "red";
    clearInterval(interval)
    timerWrap.innerHTML = ""

  } else {
    notice.textContent = "Data is being collected.";
    notice.style.color = "green";
  }
}

async function drawChart() {
  const data = await fetchData();

  const temperatureData = data.map(reading => reading.temperature);
  const pressureData = data.map(reading => reading.pressure);
  const humidityData = data.map(reading => reading.humidity);
  const timestamps = data.map(reading => formatTimestamp(reading.created_at));

  updateNotice(timestamps[timestamps.length - 1]);


  const ctx = document.getElementById('chart').getContext('2d');
  myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: timestamps,


      datasets: [
        {
          label: 'Temperature (°C)',
          data: temperatureData,
          borderColor: '#FF5733',
          fill: true,
          backgroundColor: "rgb(255, 87, 51, 0.2)",
          yAxisID: 'yl',
          tension: 0.1
        },
        {
          label: 'Pressure (hPa)',
          data: pressureData,
          borderColor: '#4A90E2',
          fill: true,
          backgroundColor: 'rgb(74, 144, 226, 0.2)',
          yAxisID: 'yr',
          tension: 0.1
        },
        {
          label: 'Humidity (%)',
          data: humidityData,
          borderColor: '#00A884',
          fill: true,
          backgroundColor: "rgb(0, 168, 132, 0.2)",
          yAxisID: 'yl',
          tension: 0.1
        }
      ]
    },
    options: {
      responsive: true,
      interaction: {
        mode: 'index',
        intersect: false,
      },
      stacked: false,
      plugins: {
        // title: {
        //   display: true,
        //   text: 'Weather Data'
        // },
        legend: {
          fontColor: "red"
        }
      },
      scales: {
        x: {
          ticks: {
            display: false
          },
          title: {
            display: true,
            text: 'Time',
            color: "#2C3E50"
          }
        },
        // 2 axis because temp and humidity are 0-50ish, pressure is ~1000
        yl: {
          type: 'linear',
          display: true,
          position: 'left',
          ticks: {
            color: "#2C3E50"
          }
        },
        yr: {
          type: 'linear',
          display: true,
          position: 'right',
          ticks: {
            color: "#2C3E50"
          },
          // so grid lines show for one axis not both (or it looks funky)
          grid: {
            drawOnChartArea: false,
          },
        },
      }
    },
  });
}

drawChart()
// // get new data every 60 seconds
// setInterval(() => {
//   if (myChart) {
//     myChart.destroy();
//     drawChart()
//   } else {
//     drawChart()
//   }
// }, 60000);


function updateTimerDisplay() {
  const minutes = Math.floor(remainingTime / 60);
  const seconds = remainingTime % 60;
  timer.textContent = `${minutes}:${seconds.toString().padStart(2, '0')}`;
}

interval = setInterval(() => {
  if (remainingTime <= 0) {
    myChart.destroy()
    drawChart()
    remainingTime = timerInital;
    updateTimerDisplay()
  } else {
    remainingTime -= 1;
    updateTimerDisplay();
  }
}, 1000);

// Initial display update
updateTimerDisplay();