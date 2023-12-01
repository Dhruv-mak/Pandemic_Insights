import "./App.css";
// import React, { useState, useEffect } from "react";
// import Tabs from "./components/Tabs";
import LandingPage from "./components/LandingPage";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Visualization from "./components/Visualization";
import TuplesCounter from "./components/TuplesCounter";
import NavBar from "./components/NavBar";
import Navbar2 from "./components/Navbar2";

function App() {
  // const [message, setMessage] = useState("");
  // useEffect(() => {
  //   fetch("/api/hello")
  //     .then((response) => {
  //       if (response.ok) {
  //         return response.json();
  //       }
  //       throw new Error("Network response was not ok.");
  //     })
  //     .then((response) => setMessage(response.message))
  //     .catch((error) => {
  //       console.error(error);
  //       setMessage("An error occurred while fetching the API.");
  //     });
  // }, []);
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<LandingPage />} />

        <Route
          exact
          path="/Doctors"
          element={<Visualization userType="Doctors" />}
        />
        <Route
          exact
          path="/Epidemiologists"
          element={<Visualization userType="Epidemiologists" />}
        />
        <Route
          exact
          path="/Policy Makers"
          element={<Visualization userType="Policy Makers" />}
        />
        <Route
          exact
          path="/General Public"
          element={<Visualization userType="General Public" />}
        />
       <Route
          exact
          path="/TuplesCounter"
          element={<Navbar2/>}
        />
      </Routes>
    </Router>
  );
}
export default App;
