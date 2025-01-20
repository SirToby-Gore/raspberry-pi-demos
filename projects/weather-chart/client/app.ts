// ! needs working on


import { createClient } from "@supabase/supabase-js";
import Chart from "chart.js/auto";

// Define the type for your reading data
interface Reading {
  temperature: number;
  pressure: number;
  humidity: number;
  created_at: string;
}

let interval: number;
let myChart: Chart;

const timer = document.getElementById("timer") as HTMLInputElement;
const timerWrap = document.getElementById("timer-wrap") as HTMLElement;
const timerInstal = 60;
let remainingTime = timerInstal;

// set up our supabase client, so we can get data from our tables
const supabase = createClient(
  import.meta.env.VITE_SUPABASE_URL,
  import.meta.env.VITE_SUPABASE_ANON_KEY
);

// get the readings data from Supabase
async function fetchData(): Promise<Reading[]> {
  const { data, error } = await supabase
    .from("readings")
    .select("temperature, pressure, humidity, created_at")
    .order("created_at", { ascending: true });

  if (error) {
    console.error("Error fetching data:", error);
    return [];
  }
  console.log(data);
  return data;
}

// love me some dates in JavaScript... /s
function formatTimestamp(timestamp: string): string {
  const date = new Date(timestamp);

  const year = date.getUTCFullYear();
  const month = String(date.getUTCMonth() + 1).padStart(2, "0"); // months are 0 indexed for some dumb reason
  const day = String(date.getUTCDate()).padStart(2, "0");
  const hours = String(date.getUTCHours()).padStart(2, "0");
  const minutes = String(date.getUTCMinutes()).padStart(2, "0");

  return `${year}-${month}-${day} ${hours}:${minutes}`;
}

// this tells the user if data is actively being collected, or if they Pi is off
function updateNotice(timestamp: string) {
  const notice = document.getElementById("data-notice") as HTMLSpanElement;
  const lastReading = new Date(timestamp);
  const now = new Date();
  const diffInSeconds = (now - lastReading) / 1000;

  if (diffInSeconds > 60) {
    notice.textContent = `Data is not being collected. Last reading ${formatTimestamp(
      lastReading
    )}.`;
    notice.style.color = "red";
    clearInterval(interval);
    timerWrap.innerHTML = "";
  } else {
    notice.textContent = "Data is being collected.";
    notice.style.color = "green";
  }
}

async function drawChart() {
  // mmm, data...
  const data = await fetchData();

  if (!data || data.length === 0) {
      console.warn("No data to draw chart.");
      return;
  }

  // create an array for each of our data types
  const temperatureData = data.map((reading) => reading.temperature);
  const pressureData = data.map((reading) => reading.pressure);
  const humidityData = data.map((reading) => reading.humidity);
  const timestamps = data.map((reading) => formatTimestamp(reading.created_at));

  updateNotice(timestamps[timestamps.length - 1]);

  // make a sweet looking chart with out sweet looking data!
  const ctx = document.getElementById("chart").getContext("2d") as CanvasRenderingContext2D;
  myChart = new Chart(ctx, {
    type: "line",
    data: {
      labels: timestamps,

      datasets: [
        {
          label: "Temperature (°C)",
          data: temperatureData,
          borderColor: "#FF5733",
          fill: true,
          backgroundColor: "rgb(255, 87, 51, 0.2)",
          yAxisID: "yl",
          tension: 0.1,
        },
        {
          label: "Pressure (hPa)",
          data: pressureData,
          borderColor: "#4A90E2",
          fill: true,
          backgroundColor: "rgb(74, 144, 226, 0.2)",
          yAxisID: "yr",
          tension: 0.1,
        },
        {
          label: "Humidity (%)",
          data: humidityData,
          borderColor: "#00A884",
          fill: true,
          backgroundColor: "rgb(0, 168, 132, 0.2)",
          yAxisID: "yl",
          tension: 0.1,
        },
      ],
    },
    options: {
      responsive: true,
      interaction: {
        mode: "index",
        intersect: false,
      },
      stacked: false,
      plugins: {
        legend: {
          fontColor: "red",
        },
      },
      scales: {
        x: {
          ticks: {
            display: false,
          },
          title: {
            display: true,
            text: "Time",
            color: "#2C3E50",
          },
        },
        // 2 axis because temp and humidity are 0-50ish, pressure is ~1000
        yl: {
          type: "linear",
          display: true,
          position: "left",
          ticks: {
            color: "#2C3E50",
          },
        },
        yr: {
          type: "linear",
          display: true,
          position: "right",
          ticks: {
            color: "#2C3E50",
          },
          // so grid lines show for one axis not both (or it looks funky)
          grid: {
            drawOnChartArea: false,
          },
        },
      },
    },
  });
}

function updateTimerDisplay() {
  const minutes = Math.floor(remainingTime / 60);
  const seconds = remainingTime % 60;
  timer.textContent = `${minutes}:${seconds.toString().padStart(2, "0")}`;
}

// initial chart creation
drawChart();

// update every 60 seconds
interval = setInterval(() => {
  if (remainingTime <= 0) {
    if (myChart) {
      myChart.destroy();
    }
    drawChart();
    remainingTime = timerInstal;
    updateTimerDisplay();
  } else {
    remainingTime -= 1;
    updateTimerDisplay();
  }
}, 1000);

// Initial display update
updateTimerDisplay();