import "../styles/RouteCard.css";

function RouteCard({ route }) {

    if (!route || !route.destination) {
        return null;
    }

    return (

        <div className="route-card">

            <h2>🚚 AI Route Recommendation</h2>

            <div className="route-row">

                <span>Destination</span>

                <strong>{route.destination}</strong>

            </div>

            <div className="route-row">

                <span>Distance</span>

                <strong>{route.distance} km</strong>

            </div>

            <div className="route-row">

                <span>Estimated Time</span>

                <strong>{route.eta} Minutes</strong>

            </div>

        </div>

    );

}

export default RouteCard;