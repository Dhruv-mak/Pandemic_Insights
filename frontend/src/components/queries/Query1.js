import React from "react";
import DropdownCheckbox from "../DropdownCheckbox";
import { get_coutry_list } from "../../services/api";
import { get_query } from "../../services/api";
import { useState, useEffect } from "react";
import Plot from "react-plotly.js";
import DatePicker from "../DatePicker";

const Query1 = () => {
  const [checkedValues, setCheckedValues] = useState([]);
  const [countries, setCountries] = useState([]);
  const [queryGraph, setQueryGraph] = useState([]);
  useEffect(() => {
    async function getCountryList() {
      const data = await get_coutry_list(1);
      setCountries(data);
    }
    getCountryList();
  }, []);
  useEffect(() => {
    async function getQueryGraph() {
      if (checkedValues.length === 0) {
        return;
      }
      const queryGraphFetched = await get_query(1, checkedValues);
      setQueryGraph(queryGraphFetched);
    }
    getQueryGraph();
  }, [checkedValues]);
  const handleCheck = (itemID) => {
    setCheckedValues((prevValues) => {
      if (prevValues.includes(itemID)) {
        return prevValues.filter((id) => id !== itemID);
      } else {
        return [...prevValues, itemID];
      }
    });
  };
  const checkboxItems = countries.map((country) => {
    return {
      id: country,
      value: country,
      checked: false,
      label: country,
    };
  });
  return (
    <div className="Visual mx-28 ">
      <div className="w-[75%] pl-3 pt-10 text-2xl text-slate-900 font-extrabold">
        Pandemic Pulse Tracker
      </div>
      <div className="w-[75%] pl-3 pt-5 text-l text-slate-900 font-bold">
        This section of our webpage presents a 'pulse tracker' on the current
        state of the pandemic globally. You can use this application to monitor
        and analyze COVID-19 data trends such as new cases, testing rates, and
        test positivity rates across different countries. With data on smoothed
        case averages and categorized testing volumes, this tool offers vital
        insights into the pandemic's status and testing efficiency.
      </div>

      <div className="flex">
        <div className="inline ml-10 mt-10">
          <DropdownCheckbox
            buttonText="Select a Country"
            checkboxItems={checkboxItems}
            handleCheck={handleCheck}
          />
        </div>

        {/* <div className="inline ml-12 mt-8 pt-2">
          <DatePicker />
        </div> */}
      </div>
      <div className="flex flex-col">
        {queryGraph.map((graph, index) => (
          <div
            className="mx-auto mt-5 rounded-2xl hover:shadow-2xl overflow-hidden"
            key={index}
          >
            <Plot
              data={graph.data}
              layout={{
                ...graph.layout,
                width: window.innerWidth * 0.65,
                height: window.innerHeight * 0.7,
              }}
            />
          </div>
        ))}
      </div>
    </div>
  );
};
export default Query1;
