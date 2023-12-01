import React from "react";
import backgroundImage from "../assets/images/background.png";
import Users from "./UserPage";
import NavBar from "./NavBar";
// import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
const LandingPage = ({ childs }) => {
  return (
    <div>
      <NavBar />
      <div
        style={{ backgroundImage: `url(${backgroundImage})` }}
        className="bg-center bg-cover bg-no-repeat h-screen relative"
        id="home"
      >
        <div className="absolute inset-0 bg-black opacity-0"></div>
        {/* {childs} */}
        <div className="pt-[10rem] pl-40 w-3/5 text- relative h-[100vh]">
          <h1 className="text-8xl text-slate-900 font-bold pb-20">
            Pandemic Insights
          </h1>
          <p className="w-[75%] pl-3 text-xl text-slate-900 font-extrabold">
          Delve into the evolving narrative of the COVID-19 pandemic with our advanced analytical tool. Harness the power of comprehensive data and sophisticated queries to uncover hidden trends and critical insights. Collaborate with us in crafting a deeper understanding of the pandemic's multifaceted impact on our world.
          </p>
        </div>

        <Users />
      </div>
    </div>
  );
};

export default LandingPage;
