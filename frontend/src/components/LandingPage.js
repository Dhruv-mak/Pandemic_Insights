import React from "react";
import Tabs from "./Tabs";
import backgroundImage from "../assets/images/background.png";
import Users from "./UserPage";
import NavBar from "./NavBar";
// import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
const LandingPage = ({ childs }) => {
  // const tabs = [
  //   {
  //     id: "tabs-profile3",
  //     href: "#home",
  //     label: "Home",
  //     isActive: true,
  //   },
  //   {
  //     id: "tabs-profile3",
  //     href: "#users",
  //     label: "Users",
  //     isActive: false,
  //   },
  //   {
  //     id: "tabs-contact3",
  //     href: "#tabs-contact3",
  //     label: "Contact",
  //     isActive: false,
  //   },
  // ];
  return (
    <div>
      {/* <div className="fixed px-40 top-0 bg-slate-800 opacity-90 z-10 w-full">
        <Tabs tabs={tabs} />
      </div> */}
      <NavBar />
      <div
        style={{ backgroundImage: `url(${backgroundImage})` }}
        className="bg-center bg-cover bg-no-repeat h-screen relative"
        id="home"
      >
        <div className="absolute inset-0 bg-black opacity-0"></div>
        {/* {childs} */}
        <div className="pt-64 pl-40 w-3/5 text- relative h-[100vh]">
          <h1 className="text-8xl text-black font-semibold pb-20">
            Pandemic Insights
          </h1>
          <p className="w-[75%] pl-3 text-xl text-black font-bold">
            chutiya marcus marcus chutiya chuthiya marcus marcus chutiya.
            chutiya marcus marcus chutiya chuthiya marcus marcus chutiya.
            chutiya marcus marcus chutiya chuthiya marcus marcus chutiya.
          </p>
        </div>

        <Users />
      </div>
    </div>
  );
};

export default LandingPage;
