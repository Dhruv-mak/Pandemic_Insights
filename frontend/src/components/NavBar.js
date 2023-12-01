import React from "react";
import Tabs from "./Tabs";
import { Link } from "react-router-dom"; 
import TuplesCounter from "./TuplesCounter"

export default function NavBar() {
  const tabs = [
    {
      id: "tabs-profile3",
      href: "#home",
      label: "Home",
      isActive: true,
    },
    {
      id: "tabs-profile3",
      href: "#users",
      label: "Users",
      isActive: false,
    },
    {
      id: "count",
      href: "#count",
      label: "Count",
      isActive: false,
    },
  ];

  return (
    <div className="fixed px-40 top-0 bg-slate-800 opacity-95 z-10 w-full">
      <Tabs tabs={tabs} />
    </div>
  );
}
