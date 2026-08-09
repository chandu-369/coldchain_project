import "../styles/Card.css";

function StatusCard({ status }) {

  const safe = status === "SAFE";

  return (

    <div
      className="card"
      style={{
        border: safe
          ? "3px solid #22c55e"
          : "3px solid #ef4444",
      }}
    >

      <h2>Current Status</h2>

      <h1
        style={{
          color: safe ? "#22c55e" : "#ef4444",
        }}
      >
        {status}
      </h1>

    </div>

  );

}

export default StatusCard;