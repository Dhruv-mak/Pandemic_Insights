import "./App.css";
// import React, { useState, useEffect } from "react";
// import Tabs from "./components/Tabs";
import LandingPage from "./components/LandingPage";

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
    <div className="scroll-smooth">
      <LandingPage></LandingPage>
    </div>
  );
}
export default App;
