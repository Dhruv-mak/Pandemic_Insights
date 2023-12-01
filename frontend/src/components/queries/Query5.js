import React from "react";
import DropdownCheckbox from "../DropdownCheckbox";
import DropdownButton from "../DropdownButton";
import { get_coutry_list } from "../../services/api";
import { get_query } from "../../services/api";
import { useState, useEffect } from "react";
import Plot from "react-plotly.js";

const Query2 = () => {
  const [checkedCountries, setCheckedCountries] = useState([]);
  const [checkedEmissionTypes, setCheckedEmissionTypes] = useState([]);
  const [countries, setCountries] = useState([]);
  const [queryGraph, setQueryGraph] = useState([]);

  useEffect(() => {
    async function getCountryList() {
      const data = await get_coutry_list(2);
      setCountries(data);
    }
    getCountryList();
  }, []);

  useEffect(() => {
    async function getQueryGraph() {
      if (checkedCountries.length === 0 || checkedEmissionTypes.length === 0) {
        return;
      }
      const queryGraphFetched = await get_query(2, checkedCountries, {
        emission_type: checkedEmissionTypes,
      });
      setQueryGraph(queryGraphFetched);
    }
    getQueryGraph();
  }, [checkedCountries, checkedEmissionTypes]);

  const handleCountryCheck = (itemID) => {
    setCheckedCountries((prevValues) => {
      if (prevValues.includes(itemID)) {
        return prevValues.filter((id) => id !== itemID);
      } else {
        return [...prevValues, itemID];
      }
    });
  };

  const handleEmissionTypeCheck = (itemID) => {
    setCheckedEmissionTypes([itemID]);
  };
  const checkboxItems = countries.map((country) => {
    return {
      id: country,
      value: country,
      checked: false,
      label: country,
    };
  });
  const emissionTypes = [
    "coal_ratio_change",
    "oil_ratio_change",
    "gas_ratio_change",
    "cement_ratio_change",
    "flaring_ratio_change",
  ];
  const emissionTypeItems = emissionTypes.map((emissionType) => {
    return {
      id: emissionType,
      value: emissionType,
      checked: false,
      label: emissionType,
    };
  });
  return (
    <div className="Visual mx-28">
      <div className="w-[75%] pl-3 pt-10 text-2xl text-slate-900 font-extrabold">
        Carbon Emission Sources Year-over-Year Analysis (CEA)
      </div>
      <div className="w-[75%] pl-3 pt-5 text-l text-slate-900 font-bold">
        This section is designed to evaluate the changes in carbon dioxide
        emissions from different sources across countries and globally over
        time. It allows users to break down emissions into categories like coal,
        oil, gas, cement, and flaring, and calculate their respective
        contributions to the total CO2 emissions. This analysis is crucial for
        understanding how different sectors contribute to overall emissions and
        for monitoring the progress of emission reduction efforts in various
        countries and on a global scale.
      </div>
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
            handleClick={handleEmissionTypeCheck}
          />
        </div>
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
export default Query2;
