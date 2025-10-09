import React from "react";
import "../assets/styles/maker.css";

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="nav-right">
        <div className="notif">
          <i className="fa-solid fa-bell"></i>
          <span className="notif-badge">3</span>
        </div>
        <div className="profile">
          <img src="" alt="user" />
          <div className="user-details">
            <h4>Account Settings</h4>
            <p>Loan Officer</p>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;


import React from "react";
import SCLogo from "../../assets/images/SC.jpg";
import "../../assets/styles/maker.css";

const Sidebar = () => {
  return (
    <aside className="sidebar">
      <div className="logo">
        <img src={SCLogo} alt="Logo" className="logo-img" />
      </div>
      <nav className="nav">
        <a className="active" href="#">Dashboard</a>
        <a href="#">Applications <span className="badge">12</span></a>
        <a href="#">Approved</a>
        <a href="#">Rejected</a>
        <a href="#">Pending</a>
        <a href="#">Reports</a>
        <a href="#">Settings</a>
      </nav>
    </aside>
  );
};

export default Sidebar;


import React from "react";
import "../../assets/styles/maker.css";

const Banner = () => {
  return <section className="banner"></section>;
};

export default Banner;


import React from "react";
import "../../assets/styles/maker.css";

const StatsCards = () => {
  return (
    <section className="stats-cards">
      <div className="card">
        <h3>Total Applications</h3>
        <p className="count">24</p>
        <span className="success">↑ 12% from last month</span>
      </div>

      <div className="card warning">
        <h3>Pending Review</h3>
        <p className="count">8</p>
        <span className="alert">⚠ Requires attention</span>
      </div>

      <div className="card success-card">
        <h3>Approved Today</h3>
        <p className="count">6</p>
        <span className="success">✅ Great progress!</span>
      </div>

      <div className="card danger">
        <h3>Rejected</h3>
        <p className="count">2</p>
        <span className="alert">❌ This month</span>
      </div>
    </section>
  );
};

export default StatsCards;




 import React from "react";
import "../../assets/styles/maker.css";

const Filters = () => {
  return (
    <div className="filters">
      <input
        type="text"
        placeholder="Search by customer name, loan type, or application ID"
      />
      <select>
        <option>All Loan Types</option>
        <option>Personal Loan</option>
        <option>Home Loan</option>
        <option>Vehicle Loan</option>
      </select>
      <select>
        <option>All Statuses</option>
        <option>Verified</option>
        <option>Pending Docs</option>
      </select>
      <button className="filter-btn">Filter</button>
    </div>
  );
};

export default Filters;



import React from "react";
import "../../assets/styles/maker.css";

const ApplicationsTable = () => {
  return (
    <section className="applications">
      <div className="section-header">
        <h2>Recent Applications</h2>
        <p>Review and process loan applications</p>
      </div>

      <table className="app-table">
        <thead>
          <tr>
            <th>Applicant</th>
            <th>Loan Type</th>
            <th>Amount</th>
            <th>Status</th>
            <th>Applied Date</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Sarah Johnson<br /><span>sarah.j@email.com</span></td>
            <td><span className="tag blue">Home Loan</span></td>
            <td>₹25,00,000</td>
            <td><span className="status pending">Pending Review</span></td>
            <td>Dec 15, 2024</td>
            <td><a href="#">Open</a></td>
          </tr>

          <tr>
            <td>Michael Chen<br /><span>m.chen@email.com</span></td>
            <td><span className="tag green">Personal Loan</span></td>
            <td>₹5,00,000</td>
            <td><span className="status approved">Approved</span></td>
            <td>Dec 14, 2024</td>
            <td><a href="#">Open</a></td>
          </tr>

          <tr>
            <td>David Wilson<br /><span>d.wilson@email.com</span></td>
            <td><span className="tag purple">Vehicle Loan</span></td>
            <td>₹8,50,000</td>
            <td><span className="status pending">Pending Review</span></td>
            <td>Dec 13, 2024</td>
            <td><a href="#">Open</a></td>
          </tr>

          <tr>
            <td>Emma Brown<br /><span>e.brown@email.com</span></td>
            <td><span className="tag blue">Home Loan</span></td>
            <td>₹12,00,000</td>
            <td><span className="status rejected">Rejected</span></td>
            <td>Dec 12, 2024</td>
            <td><a href="#">Open</a></td>
          </tr>
        </tbody>
      </table>

      <div className="pagination">
        <button id="prev-btn">Previous</button>
        <button id="next-btn">Next</button>
      </div>
    </section>
  );
};

export default ApplicationsTable;



                      
            

            
                    

import React from "react";
import Navbar from "../../common/Navbar";
import Sidebar from "../../components/maker/Sidebar";
import Banner from "../../components/maker/Banner";
import StatsCards from "../../components/maker/StatsCards";
import Filters from "../../components/maker/Filters";
import ApplicationsTable from "../../components/maker/ApplicationsTable";
import "../../assets/styles/maker.css";

const MakerDashboard = () => {
  return (
    <div className="maker-dashboard">
      <Navbar />
      <div className="dashboard-container">
        <Sidebar />
        <main className="main-content">
          <Banner />
          <StatsCards />
          <Filters />
          <ApplicationsTable />
        </main>
      </div>
    </div>
  );
};

export default MakerDashboard;




import React from "react";
import MakerDashboard from "./pages/maker/MakerDashboard";

function App() {
  return <MakerDashboard />;
}

export default App;



                    
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./index.css";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

                           
                                                
                      
