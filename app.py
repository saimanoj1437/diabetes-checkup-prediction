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



/* ============ Global Styles ============ */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Inter', sans-serif;
}

body {
  background: #f5f7fb;
  color: #333;
  display: flex;
  min-height: 100vh;
}

/* =================== Sidebar =================== */
.sidebar {
  width: 220px;
  background: #fff;
  padding: 20px;
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
  position: fixed;
  top: 0;
  left: 0;
  height: 100%;
  z-index: 200;
}

.sidebar .logo {
  text-align: center;
  margin-bottom: 30px;
}

.sidebar .logo img {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  object-fit: cover;
}

.sidebar nav a {
  display: flex;
  justify-content: space-between;
  align-items: center;
  text-decoration: none;
  color: #333;
  padding: 10px 15px;
  border-radius: 6px;
  margin-bottom: 10px;
  transition: 0.3s;
}

.sidebar nav a.active,
.sidebar nav a:hover {
  background: #07b132;
  color: #fff;
}

.sidebar nav .badge {
  background: red;
  color: #fff;
  font-size: 12px;
  padding: 2px 6px;
  border-radius: 12px;
}

/* =================== Content Wrapper =================== */
.maker-dashboard {
  display: flex;
  width: 100%;
}

.dashboard-container {
  display: flex;
  width: 100%;
}

.main-content {
  margin-left: 220px;
  width: calc(100% - 220px);
  flex: 1;
  display: flex;
  flex-direction: column;
  background: #f5f7fb;
}

/* =================== Navbar =================== */
.navbar {
  background: #fff;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  padding: 12px 40px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  position: sticky;
  top: 0;
  z-index: 100;
  border-left: 1px solid transparent;
}

.nav-right {
  display: flex;
  align-items: center;
  gap: 20px;
}

.notif {
  position: relative;
  font-size: 1.3rem;
  color: #0078d7;
  cursor: pointer;
}

.notif-badge {
  position: absolute;
  top: -6px;
  right: -8px;
  background: red;
  color: white;
  font-size: 10px;
  border-radius: 50%;
  padding: 2px 5px;
}

.profile {
  display: flex;
  align-items: center;
  gap: 10px;
}

.profile img {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: #ccc;
}

.user-details h4 {
  font-size: 14px;
}

.user-details p {
  font-size: 12px;
  color: #777;
}

/* =================== Banner =================== */
.banner {
  background: url("https://sustainability-news.net/wp-content/uploads/2024/08/SC-head-office-2022-scaled-1.jpg") no-repeat center center;
  background-size: cover;
  height: 30vh;
  position: relative;
}

/* =================== Stats Cards =================== */
.stats-cards {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-top: -50px;
  position: relative;
  z-index: 10;
}

.card {
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  text-align: center;
  width: 250px;
}

.card h3 {
  font-size: 14px;
  color: #555;
}

.count {
  font-size: 22px;
  font-weight: 700;
  margin: 6px 0;
}

.success {
  color: #1e7c4c;
}

.warning {
  border-left: 4px solid #e97724;
}

.success-card {
  border-left: 4px solid #1e7c4c;
}

.danger {
  border-left: 4px solid #e34242;
}

/* =================== Filters =================== */
.filters {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px 20px;
  background: #fff;
  justify-content: space-between;
  border-bottom: 1px solid #e5e7eb;
  margin-top: 10px;
  border-radius: 8px;
}

.filters input {
  flex: 1;
  padding: 10px;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  outline: none;
}

.filters select {
  padding: 10px;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  outline: none;
}

.filter-btn {
  background: #2563eb;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 8px;
  cursor: pointer;
  transition: 0.3s;
}

.filter-btn:hover {
  background: black;
  color: white;
}

/* =================== Applications Section =================== */
.applications {
  background: #fff;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  margin: 40px 60px;
}

.section-header h2 {
  font-size: 18px;
  color: #0078d7;
}

.section-header p {
  font-size: 13px;
  color: #888;
}

/* =================== Table =================== */
.app-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

.app-table th,
.app-table td {
  padding: 10px;
  text-align: left;
  border-bottom: 1px solid #eee;
  font-size: 14px;
}

.tag {
  padding: 4px 8px;
  border-radius: 6px;
  font-size: 12px;
  color: white;
}

.blue {
  background: #3b82f6;
}

.green {
  background: #16a34a;
}

.purple {
  background: #8b5cf6;
}

.status {
  padding: 4px 8px;
  border-radius: 6px;
  font-size: 12px;
  color: white;
}

.pending {
  background: #facc15;
  color: #333;
}

.approved {
  background: #16a34a;
}

.rejected {
  background: #e34242;
}

/* =================== Pagination =================== */
.pagination {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 15px;
}

.pagination button {
  padding: 6px 12px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  background: #f0f2f5;
  transition: 0.3s;
}

.pagination button:hover {
  background: #0078d7;
  color: white;
}
                      
