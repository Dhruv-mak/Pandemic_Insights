import React, { useState } from "react";
import Navbar2 from "./Navbar2";
import QueryTabs from "./QueryTabs";
import Query1 from "./queries/Query1";
import Query2 from "./queries/Query2";
import Query3 from "./queries/Query3";
import Query4 from "./queries/Query4";
import Query5 from "./queries/Query5";
import Query6 from "./queries/Query6";
export default function Visualization({ userType }) {
  const tabs = [
    { id: "query1", href: "#query1", label: "Query1" },
    { id: "query2", href: "#query2", label: "Query2" },
    { id: "query3", href: "#query3", label: "Query3" },
    { id: "query4", href: "#query4", label: "Query4" },
    { id: "query5", href: "#query5", label: "Query5" },
    { id: "query6", href: "#query6", label: "Query6" },
  ];

  const queryMap = {
    Doctors: [0, 1, 2],
    Epidemiologists: [0, 1, 2, 3],
    "Policy Makers": [0, 1, 2, 3, 4, 5],
    "General Public": [0, 4],
  };

  const UserTabs = getUserTabs(queryMap[userType], tabs);

  const [selectedTab, setSelectedTab] = useState(UserTabs[0].id);

  const handleClick = (tab) => {
    setSelectedTab(tab.id);
  };

  return (
    <div className="Visual bg-[#c8becc] bg-gradient-to-br from-[#cebd5dab] via-[#ffffff] to-[#1697a3b6] min-h-screen">
      <div>
        <Navbar2 />
      </div>
      <div className="fixed px-40 top-0 bg-slate-800 opacity-90 z-10 w-full mt-[5.25rem]">
        <QueryTabs
          tabs={UserTabs}
          handleClick={handleClick}
          selectedTab={selectedTab}
        />
      </div>
      <div className="pt-36">
        {selectedTab === "query1" && <Query1 />}
        {selectedTab === "query2" && (
          <div>
            <Query2 />
          </div>
        )}
        {selectedTab === "query3" && (
          <div>
            <Query3 />
          </div>
        )}
        {selectedTab === "query4" && (
          <div>
            <Query4 />
          </div>
        )}
        {selectedTab === "query5" && (
          <div>
            <Query5 />
          </div>
        )}
        {selectedTab === "query6" && (
          <div>
            <Query6 />
          </div>
        )}
      </div>
    </div>
  );
}

const getUserTabs = (userMap, tabs) => {
  return userMap.map((index) => tabs[index]);
};
