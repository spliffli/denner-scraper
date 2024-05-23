# denner-scraper
A single-use web scraper which gets the contact information of all the Denner Sattelit, Partner & Express stores in Switzerland because it's recently become a requirement at my day job to contact all of them, and currently my colleagues are doing it by manually reading and typing each contact into HubSpot CRM one by one which would take ages.

---

## Steps

- [x] With selenium webdriver, navigate to [https://www.denner.ch/de/filialen/](https://www.denner.ch/de/filialen/)

- [x] Apply the filters to show only the Sattelit, Partner & Express stores, and not the other types. This is given as a big list on one page which makes it fairly simple.

- [ ] Iterate through the entire list: 
    - [ ] extract data points from the dom/html, using either class, id or xpath selectors 
    - [ ] add each data point as column values for a new row in a pandas dataframe.

- [ ] Possibly clean the data if it needs it, or that could be left until after the next step. 

- [ ] Save the dataframe in .xls or .xlsx format

- [ ] Do some validation check e.g. make sure it's the correct amount of rows

- [ ] Review the created excel sheet to make sure it's prepared and compatible with HubSpot.

- [ ] Import all the contacts into Hubspot at once from the excel file, saving weeks of time.

