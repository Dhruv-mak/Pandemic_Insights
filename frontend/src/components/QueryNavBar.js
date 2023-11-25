import React from "react";
import QueryTabs from "./QueryTabs";

export default function QueryNavBar() {
  const tabs = [
    
    {
      id: "query1",
      href: "#query1",
      label: "Query1",
      isActive: true,
    },
    {
      id: "query2",
      href: "#query2",
      label: "Query2",
      isActive: true,
    },
    {
      id: "query3",
      href: "#query3",
      label: "Query3",
      isActive: true,
    },
    {
      id: "query4",
      href: "#query4",
      label: "Query4",
      isActive: true,
    },
    {
      id: "query5",
      href: "#query5",
      label: "Query5",
      isActive: true,
    }
  ];

  return (
    <div className="fixed px-40 top-0 bg-slate-800 opacity-90 z-10 w-full mt-[4.25rem]">
      <QueryTabs tabs={tabs} />
    </div>
  );
}
