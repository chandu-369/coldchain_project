import "../styles/Card.css";

function InfoCard({icon,title,value}){

    return(

        <div className="card">

            <div className="cardIcon">

                {icon}

            </div>

            <h3>{title}</h3>

            <h2>{value}</h2>

        </div>

    );

}

export default InfoCard;