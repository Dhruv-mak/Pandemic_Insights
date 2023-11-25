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
    // {
    //   id: "tabs-profile3",
    //   href: "#query1",
    //   label: "Query1",
    //   isActive: true,
    // },
    // {
    //   id: "tabs-profile3",
    //   href: "#query2",
    //   label: "Query2",
    //   isActive: true,
    // },
    // {
    //   id: "tabs-profile3",
    //   href: "#query3",
    //   label: "Query3",
    //   isActive: true,
    // },
    // {
    //   id: "tabs-profile3",
    //   href: "#query4",
    //   label: "Query4",
    //   isActive: true,
    // },
    // {
    //   id: "tabs-profile3",
    //   href: "#query5",
    //   label: "Query5",
    //   isActive: true,
    // }
  ];

  return (
    <div className="fixed px-40 top-0 bg-slate-800 opacity-90 z-10 w-full">
      <Tabs2 tabs={tabs} />
    </div>
  );
}
