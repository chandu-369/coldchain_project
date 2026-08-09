import "../styles/Card.css";

function AlertCard({status}){

    let color="#22c55e";

    if(status==="WARNING")
        color="#facc15";

    if(status==="HIGH TEMPERATURE")
        color="#ef4444";

    return(

        <div
            className="card"
            style={{
                border:`3px solid ${color}`
            }}
        >

            <h2>Current Status</h2>

            <h1
                style={{
                    color:color
                }}
            >
                {status}
            </h1>

        </div>

    );

}

export default AlertCard;