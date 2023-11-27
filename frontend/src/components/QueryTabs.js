import React from "react";

const Tabs = ({ tabs, handleClick, selectedTab }) => {
  return (
    <div className="">
      <div className="flex flex-row">
        <ul
          className="mb-4 flex flex-row list-none border-b-0 pl-0"
          role="tablist"
          data-te-nav-ref
        >
          {tabs.map((tab, index) => (
              <li 
                key={index} 
                role="tab" 
                onClick={() => handleClick(tab)} 
                className={`block border-x-0 border-b-2 border-t-0 px-7 pb-3.5 pt-4 text-md font-medium uppercase leading-tight text-neutral-300 hover:border-slate-500 hover:bg-purple-400 cursor-pointer ${selectedTab === tab.id ? 'border-purple-500' : 'border-transparent'}`}
              >
                {tab.label}
              </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Tabs;
