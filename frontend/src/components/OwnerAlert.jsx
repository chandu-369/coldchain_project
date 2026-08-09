import { useState } from "react";
import axios from "axios";

function OwnerAlert({ prediction }) {
  const [status, setStatus] = useState("");
  const [loading, setLoading] = useState(false);

  // No prediction data
  if (!prediction) {
    return null;
  }

  // Show owner alert only for HIGH risk
  if (prediction.risk !== "HIGH") {
    return null;
  }

  // ==============================
  // APPROVE REROUTE
  // ==============================

  const approve = async () => {
    try {
      setLoading(true);
      setStatus("Sending approval...");

      const response = await axios.post(
        "http://127.0.0.1:8000/reroute/approve"
      );

      setStatus(
        response.data.message || "Owner Approved Reroute"
      );

    } catch (error) {
      console.error("Approve Error:", error);

      setStatus(
        "❌ Failed to approve reroute"
      );

    } finally {
      setLoading(false);
    }
  };

  // ==============================
  // REJECT REROUTE
  // ==============================

  const reject = async () => {
    try {
      setLoading(true);
      setStatus("Sending rejection...");

      const response = await axios.post(
        "http://127.0.0.1:8000/reroute/reject"
      );

      setStatus(
        response.data.message || "Owner Rejected Reroute"
      );

    } catch (error) {
      console.error("Reject Error:", error);

      setStatus(
        "❌ Failed to reject reroute"
      );

    } finally {
      setLoading(false);
    }
  };

  // ==============================
  // UI
  // ==============================

  return (
    <div className="owner-alert">

      <h2>🚨 OWNER ALERT</h2>

      <h3>AI Prediction</h3>

      <p>
        Current Temperature:
        <b>
          {" "}
          {prediction.current} °C
        </b>
      </p>

      <p>
        Predicted Temperature:
        <b>
          {" "}
          {prediction.predicted} °C
        </b>
      </p>

      <p>
        Temperature Trend:
        <b>
          {" "}
          {prediction.trend}
        </b>
      </p>

      <p>
        Risk:
        <b
          style={{
            color: "red",
            marginLeft: "8px"
          }}
        >
          {prediction.risk}
        </b>
      </p>

      <p>
        Estimated Breach:
        <b>
          {" "}
          {prediction.minutes_to_breach !== null
            ? `${prediction.minutes_to_breach} minutes`
            : "Unknown"}
        </b>
      </p>

      {/* ============================== */}
      {/* OWNER BUTTONS */}
      {/* ============================== */}

      <div className="owner-buttons">

        <button
          onClick={approve}
          className="approve-btn"
          disabled={loading}
        >
          {loading
            ? "Processing..."
            : "✅ Approve Reroute"}
        </button>

        <button
          onClick={reject}
          className="reject-btn"
          disabled={loading}
        >
          {loading
            ? "Processing..."
            : "❌ Reject"}
        </button>

      </div>

      {/* ============================== */}
      {/* RESPONSE */}
      {/* ============================== */}

      {status && (
        <div className="owner-response">
          <h3>{status}</h3>
        </div>
      )}

    </div>
  );
}

export default OwnerAlert;