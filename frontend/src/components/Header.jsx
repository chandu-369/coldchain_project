import "../styles/Header.css";
import { FaTruck, FaCircle } from "react-icons/fa";

function Header() {

  const currentTime = new Date().toLocaleTimeString();

  return (

    <div className="header">

      <div className="header-left">

        <FaTruck className="truck-icon" />

        <h1>Cold Chain Monitoring Dashboard</h1>

      </div>

      <div className="header-right">

        <div className="status">

          <FaCircle className="online" />

          <span>Connected</span>

        </div>

        <div className="time">

          {currentTime}

        </div>

      </div>

    </div>

  );

}

export default Header;