import React from "react";
import Navbar2 from "./Navbar2";
import QueryTabs from "./QueryTabs";
import { useState, useEffect } from "react";
import Query1 from "./queries/Query1";

export default function Visualization({ userType }) {
  console.log(userType)
  const tabs = [
    { id: "query1", href: "#query1", label: "Query1", isActive: true },
    { id: "query2", href: "#query2", label: "Query2", isActive: true },
    { id: "query3", href: "#query3", label: "Query3", isActive: true },
    { id: "query4", href: "#query4", label: "Query4", isActive: true },
    { id: "query5", href: "#query5", label: "Query5", isActive: true },
  ];

  const queryMap = {
    "Doctors": [0, 1, 2],
    "Epidemiologists": [0, 1, 2, 3],
    "Policy Makers": [0, 1, 2, 3, 4],
    "General Public": [0, 4],
  };

  const UserTabs = getUserTabs(queryMap[userType], tabs);

  return (
    <div className="Visual">
      <div>
        <Navbar2 />
      </div>
      <div className="fixed px-40 top-0 bg-slate-800 opacity-90 z-10 w-full mt-[4.25rem]">
        <QueryTabs tabs={UserTabs} />
      </div>
      <div className="pt-36">
        <Query1 />
      </div>
    </div>
  );
}

const getUserTabs = (userMap, tabs) => {
  return userMap.map((index) => tabs[index]);
};