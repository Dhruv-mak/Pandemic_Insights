import React from "react";
import DropdownCheckbox from "../DropdownCheckbox";
import DropdownButton from "../DropdownButton";
import { get_coutry_list } from "../../services/api";
import { get_query } from "../../services/api";
import { useState, useEffect } from "react";
import Plot from "react-plotly.js";

const Query2 = () => {
  const [checkedCountries, setCheckedCountries] = useState([]);
  const [checkedInteractionTypes, setCheckedInteractionTypes] = useState([]);
  const [countries, setCountries] = useState([]);
  const [queryGraph, setQueryGraph] = useState([]);

  useEffect(() => {
    async function getCountryList() {
      const data = await get_coutry_list(3);
      setCountries(data);
    }
    getCountryList();
  }, []);

  useEffect(() => {
    async function getQueryGraph() {
      if (checkedCountries.length === 0) {
        return;
      }
      const queryGraphFetched = await get_query(3, checkedCountries, {
        interaction_type: checkedInteractionTypes,
      });
      setQueryGraph(queryGraphFetched);
    }
    getQueryGraph();
  }, [checkedCountries, checkedInteractionTypes]);

  const handleCountryCheck = (itemID) => {
    setCheckedCountries((prevValues) => {
      if (prevValues.includes(itemID)) {
        return prevValues.filter((id) => id !== itemID);
      } else {
        return [...prevValues, itemID];
      }
    });
  };

  const handleInteractionTypeCheck = (itemID) => {
    setCheckedInteractionTypes([itemID])
  };
  const checkboxItems = countries.map((country) => {
    return {
      id: country,
      value: country,
      checked: false,
      label: country,
    };
  });
  const interactionTypes = [
    "gdp_death_interaction",
    "cardiovasc_death_interaction",
    "diabetes_death_interaction",
    "hospital_beds_death_interaction",
  ];
  const emissionTypeItems = interactionTypes.map((emissionType) => {
    return {
      id: emissionType,
      value: emissionType,
      checked: false,
      label: emissionType,
    };
  });
  return (
    <div className="Visual mx-28">
      <div className="ml-10 mt-10">
        <DropdownCheckbox
          buttonText="Select a Country"
          checkboxItems={checkboxItems}
          handleCheck={handleCountryCheck}
        />
        <div className="mx-5 inline">
        <DropdownButton
          buttonText="Select an Emission Type"
          items={emissionTypeItems}
          handleClick={handleInteractionTypeCheck}
        />
        </div>
      </div>
      <div className="flex flex-col">
        {queryGraph.map((graph, index) => (
          <div className="mx-auto mt-5 rounded-2xl hover:shadow-2xl overflow-hidden" key={index}>
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
export default Query2;