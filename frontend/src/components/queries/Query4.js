import React from "react";
import DropdownCheckbox from "../DropdownCheckbox";
import { get_coutry_list } from "../../services/api";
import { get_query } from "../../services/api";
import { useState, useEffect } from "react";
import Plot from "react-plotly.js";

const Query1 = () => {
  const [checkedValues, setCheckedValues] = useState([]);
  const [countries, setCountries] = useState([]);
  const [queryGraph, setQueryGraph] = useState([]);
  useEffect(() => {
    async function getCountryList() {
      const data = await get_coutry_list(6);
      setCountries(data);
    }
    getCountryList();
  }, []);
  useEffect(() => {
    async function getQueryGraph() {
      if (checkedValues.length === 0) {
        return;
      }
      const queryGraphFetched = await get_query(6, checkedValues);
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
    <div className="Visual mx-28">
      <div className="w-[75%] pl-3 pt-10 text-2xl text-slate-900 font-extrabold">
        Vaccination Impact on Excess Mortality Trend Analysis (VIEM){" "}
      </div>
      <div className="w-[75%] pl-3 pt-5 text-l text-slate-900 font-bold">
        This section is designed to examine the correlation between vaccination
        rates and changes in excess mortality due to COVID-19. It allows users
        to calculate the weekly changes in both the cumulative estimated daily
        excess deaths per 100K population and the number of people vaccinated in
        specified countries. The section aims to allow users to analyze how
        increases or decreases in vaccination rates may influence the trend in
        excess mortality. This analysis is crucial for understanding the
        effectiveness of vaccination campaigns in mitigating COVID-19 related
        deaths.
      </div>
      <div className="ml-10 mt-10">
        <DropdownCheckbox
          buttonText="Select a Country"
          checkboxItems={checkboxItems}
          handleCheck={handleCheck}
        />
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
