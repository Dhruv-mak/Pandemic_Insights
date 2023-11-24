import "./App.css";
// import React, { useState, useEffect } from "react";
// import Tabs from "./components/Tabs";
import LandingPage from "./components/LandingPage";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Visualization from "./components/Visualization";

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
        <Route exact path="/" element={<LandingPage/>} />
       
       
        <Route exact path="/Doctors" element={<Visualization />}/>
        <Route exact path="/Epidemiologists" element={<Visualization />}/>
        <Route exact path="/Policy Makers" element={<Visualization />}/>
        <Route exact path="/General Public" element={<Visualization />}/>
          

      </Routes>
    </Router>
  );
}
export default App;
