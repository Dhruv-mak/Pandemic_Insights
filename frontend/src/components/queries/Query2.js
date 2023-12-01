import React from "react";
import DropdownCheckbox from "../DropdownCheckbox";
import { get_coutry_list } from "../../services/api";
import { get_query } from "../../services/api";
import { useState, useEffect } from "react";
import Plot from "react-plotly.js";
import DropdownButton from "../DropdownButton";

const Query1 = () => {
  const [checkedValues, setCheckedValues] = useState([]);
  const [countries, setCountries] = useState([]);
  const [queryGraph, setQueryGraph] = useState([]);
  const [indicators, setIndicators] = useState([]);
  useEffect(() => {
    async function getCountryList() {
      const data = await get_coutry_list(5);
      setCountries(data);
    }
    getCountryList();
  }, []);
  useEffect(() => {
    async function getQueryGraph() {
      if (checkedValues.length === 0 || indicators.length === 0) {
        return;
      }
      const queryGraphFetched = await get_query(5, checkedValues, {indicators: indicators});
      setQueryGraph(queryGraphFetched);
    }
    getQueryGraph();
  }, [checkedValues, indicators]);
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
  const items = [
    {
      id: "le",
      label: "Life Expenntacy at Birth",
    },
    {
      id: "eys",
      label: "Expected Years of Schooling",
    },
    {
      id: "mys",
      label: "Mean Years of Schooling",
    },
    {
      id: "gnipc",
      label: "Gross National Income per Capita",
    },
    {
      id: "abr",
      label: "Adolescent Birth Rate",
    },
    {
      id: "mmr",
      label: "Maternal Mortality Ratio",
    },
    {
      id: "prf",
      label: "Share of Seats in Parliament(Female)",
    },
    {
      id: "sef",
      label: "Some Secondary Education(Female)"
    },
    {
      id: "prm",
      label: "Share of Seats in Parliament(Male)"
    },
    {
      id: "sem",
      label: "Some Secondary Education(Male)"
    },
    {
      id: "lfprf",
      label: "Labor Force Participation(Female)"
    },
    {
      id: "lfprm",
      Label: "Labor Force Participation(Male)"
    }
  ]
  const handleItemClick = (item) => {
    setIndicators(item);
    console.log(item);
  }
  return (
    <div className="Visual mx-28">
      <div className="w-[75%] pl-3 pt-10 text-2xl text-slate-900 font-extrabold">
        GII Calculator (Gender Inequality Index Calculator)
      </div>
      <div className="w-[75%] pl-3 pt-5 text-l text-slate-900 font-bold">
        This section is designed to compute the Gender Inequality Index for
        selected countries. It assesses disparities in health, empowerment, and
        labor force participation between genders. The calculation meticulously
        adjusts for zero and extreme values and uses geometric and harmonic mean
        calculations to ensure accuracy. It offers a comprehensive measure of
        gender-based inequality, crucial for social research and policy-making.
      </div>
      <div className="inline ml-10 mt-10">
        <DropdownCheckbox
          buttonText="Select a Country"
          checkboxItems={checkboxItems}
          handleCheck={handleCheck}
        />
      </div>
      <div className="inline ml-5">
        <DropdownButton
        buttonText="Indicators"
        items={items}
        handleClick={handleItemClick}
        />
      </div>
      <div className="flex flex-col">
        {queryGraph.map((graph, index) => (
          <div className="mx-auto" key={index}>
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
