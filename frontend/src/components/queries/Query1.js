import React from "react";
import DropdownCheckbox from "../DropdownCheckbox";
import { get_coutry_list } from "../../services/api";
import { useState, useEffect } from "react";

const Query1 = () => {
    const [checkedValues, setCheckedValues] = useState([]);
    const [countries, setCountries] = useState([]);
    useEffect(() => {
        async function getCountryList() {
        const data = await get_coutry_list(1);
        console.log(data)
        setCountries(data);
        }
        getCountryList();
    }, []);
    useEffect(() => {
        function getCheckedValues() {
        console.log(checkedValues);
        }
        getCheckedValues();
    }, [checkedValues]);
    const handleCheck = (itemID) => {
        setCheckedValues((prevValues) => {
        if (prevValues.includes(itemID)) {
            return prevValues.filter((id) => id !== itemID);
        }
        else {
            return [...prevValues, itemID];
        }
        }
        );
    }
    const checkboxItems = countries.map((country) => {
        return {
        id: country,
        value: country,
        checked: false,
        label: country,
        }
    });
    return (
        <div className="Visual">
        <div className="">
            <DropdownCheckbox
            buttonText="Select a Country"
            checkboxItems={checkboxItems}
            handleCheck={handleCheck}
            />
        </div>
        </div>
    );
}
export default Query1;