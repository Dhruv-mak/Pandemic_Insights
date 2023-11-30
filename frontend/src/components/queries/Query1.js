import React from "react";
import DropdownCheckbox from "../DropdownCheckbox";
import { get_coutry_list } from "../../services/api";
import { get_query } from "../../services/api";
import { useState, useEffect} from "react";
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
    <div className="Visual mx-28">
      <div className="ml-28 mt-10">
        <DropdownCheckbox
          buttonText="Select a Country"
          checkboxItems={checkboxItems}
          handleCheck={handleCheck}
        />
      </div>
      <div className="flex flex-col">
        {queryGraph.map((graph, index) => (
          <div className="mx-auto" key={index}>
            <Plot 
              data={graph.data} 
              layout={{...graph.layout, width: window.innerWidth * 0.65, height: window.innerHeight * 0.7}}
            />
          </div>
        ))}
      </div>
    </div>
  );
};
export default Query1;