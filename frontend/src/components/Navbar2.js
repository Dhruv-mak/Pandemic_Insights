import React from "react";
import Tabs2 from "./Tabs2";

export default function Navbar2() {
  const tabs = [
    {
      id: "tabs-profile3",
      href: "#home",
      label: "Home",
      isActive: true,
    }
 
  ];

  return (
    <div className="fixed px-40 top-0 bg-slate-800 opacity-95 z-10 w-full">
      <Tabs2 tabs={tabs} />
    </div>
  );
}
