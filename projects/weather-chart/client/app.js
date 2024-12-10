const supabase = supabase.createClient(import.meta.env.SUPABASE_URL, import.meta.env.SUPABASE_ANON_KEY);

async function fetchData() {
  // Fetch data from the SensorReadings table
  const { data, error } = await supabase
    .from('SensorReadings')
    .select('temperature, pressure, humidity, timestamp')
    .order('timestamp', { ascending: true });

  if (error) {
    console.error("Error fetching data:", error);
    return [];
  }

  return data;
}

function updateNotice(lastTimestamp) {
  const notice = document.getElementById("data-notice");
  const lastTime = new Date(lastTimestamp);
  const now = new Date();
  const diffInSeconds = (now - lastTime) / 1000;

  if (diffInSeconds > 60) {
    notice.textContent = "Data is not being collected (last entry over 60 seconds ago).";
    notice.style.color = "red";
  } else {
    notice.textContent = "Data is being collected.";
    notice.style.color = "green";
  }
}

async function drawChart() {
  const data = await fetchData();

  const timestamps = data.map(entry => entry.timestamp);
  const temperatures = data.map(entry => entry.temperature);
  const pressures = data.map(entry => entry.pressure);
  const humidities = data.map(entry => entry.humidity);

  updateNotice(timestamps[timestamps.length - 1]);

  const ctx = document.getElementById('weatherChart').getContext('2d');
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: timestamps,
      datasets: [
        {
          label: 'Temperature (°C)',
          data: temperatures,
          borderColor: 'red',
          fill: false
        },
        {
          label: 'Pressure (hPa)',
          data: pressures,
          borderColor: 'blue',
          fill: false
        },
        {
          label: 'Humidity (%)',
          data: humidities,
          borderColor: 'green',
          fill: false
        }
      ]
    },
    options: {
      scales: {
        x: {
          type: 'time',
          time: {
            unit: 'minute'
          },
          title: {
            display: true,
            text: 'Time'
          }
        },
        y: {
          title: {
            display: true,
            text: 'Values'
          }
        }
      }
    }
  });
}

document.addEventListener('DOMContentLoaded', drawChart);