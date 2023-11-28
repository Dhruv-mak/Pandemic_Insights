import React from "react";
import DropdownCheckbox from "../DropdownCheckbox";
import { get_coutry_list } from "../../services/api";
import { get_query } from "../../services/api";
import { useState, useEffect, useRef } from "react";
import Plot from "react-plotly.js";

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
  const isFirstRender = useRef(true);
  useEffect(() => {
    if (isFirstRender.current) {
      isFirstRender.current = false;
      return;
    }
    async function getQueryGraph() {
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
    <div className="Visual">
      <div className="ml-10 mt-10">
        <DropdownCheckbox
          buttonText="Select a Country"
          checkboxItems={checkboxItems}
          handleCheck={handleCheck}
        />
      </div>
      <Plot data={queryGraph.data} layout={queryGraph.layout}></Plot>
    </div>
  );
};
export default Query1;