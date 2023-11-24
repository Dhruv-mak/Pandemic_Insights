import React from "react";
import Tabs from "./Tabs";

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
      id: "tabs-contact3",
      href: "#tabs-contact3",
      label: "Contact",
      isActive: false,
    },
  ];

  return (
    <div className="fixed px-40 top-0 bg-slate-800 opacity-90 z-10 w-full">
      <Tabs tabs={tabs} />
    </div>
  );
}
