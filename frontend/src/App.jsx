import { useEffect, useState } from "react";
import axios from "axios";

import Header from "./components/Header";
import InfoCard from "./components/InfoCard";
import StatusCard from "./components/StatusCard";
import OwnerAlert from "./components/OwnerAlert";
import RouteCard from "./components/RouteCard";

import "./App.css";
import "./styles/OwnerAlert.css";
import "./styles/RouteCard.css";

function App() {

  const [telemetry, setTelemetry] = useState({});
  const [prediction, setPrediction] = useState(null);
  const [route, setRoute] = useState(null);

  useEffect(() => {

    const loadData = async () => {

      try {

        const telemetryRes = await axios.get(
          "http://127.0.0.1:8000/telemetry/latest"
        );

        setTelemetry(telemetryRes.data);

        const predictionRes = await axios.get(
          "http://127.0.0.1:8000/prediction"
        );

        setPrediction(predictionRes.data);

        const routeRes = await axios.get(
          "http://127.0.0.1:8000/route"
        );

        setRoute(routeRes.data);

      } catch (error) {

        console.log(error);

      }

    };

    loadData();

    const timer = setInterval(loadData, 2000);

    return () => clearInterval(timer);

  }, []);

  return (

    <div className="container">

      <Header />

      <div className="dashboard-grid">

        <InfoCard
          title="Vehicle"
          value={telemetry.vehicleId}
          icon="🚚"
        />

        <InfoCard
          title="Medicine"
          value={telemetry.medicine}
          icon="💊"
        />

        <InfoCard
          title="Temperature"
          value={`${telemetry.temperature} °C`}
          icon="🌡️"
        />

        <InfoCard
          title="Humidity"
          value={`${telemetry.humidity} %`}
          icon="💧"
        />

        <InfoCard
          title="Latitude"
          value={telemetry.latitude}
          icon="📍"
        />

        <InfoCard
          title="Longitude"
          value={telemetry.longitude}
          icon="🧭"
        />

        <InfoCard
          title="Timestamp"
          value={telemetry.timestamp}
          icon="🕒"
        />

        <StatusCard
          status={telemetry.status}
        />

      </div>

      <OwnerAlert
        prediction={prediction}
      />

      <RouteCard
        route={route}
      />

    </div>

  );

}

export default App;