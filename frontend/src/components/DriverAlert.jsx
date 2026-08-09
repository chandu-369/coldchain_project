import { useEffect, useState } from "react";
import axios from "axios";

function DriverAlert() {

  const [reroute, setReroute] = useState(null);

  useEffect(() => {

    const loadStatus = async () => {

      try {

        const res = await axios.get(
          "http://127.0.0.1:8000/reroute"
        );

        setReroute(res.data);

      } catch (err) {

        console.log(err);

      }

    };

    loadStatus();

    const timer = setInterval(loadStatus,2000);

    return ()=>clearInterval(timer);

  },[]);

  if(!reroute) return null;

  if(!reroute.approved) return null;

  return(

    <div className="driver-alert">

      <h2>🚚 DRIVER ALERT</h2>

      <h3>Owner Approved Reroute</h3>

      <p>

        Proceed to the nearest cold storage facility immediately.

      </p>

      <button>

        ACKNOWLEDGE

      </button>

    </div>

  );

}

export default DriverAlert;