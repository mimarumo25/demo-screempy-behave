from screenpy_selenium import Target

TXT_BUSINESS_NAME = Target.the("business name field").located_by("//input[@id='Serenity_Pro_Organization_BusinessUnitDialog3_Name']")
TXT_BUSINESS_UNIT = Target.the("business unit div").located_by("//div[@class='field ParentUnitId']//div")
LST_BUSINESS_UNIT = Target.the("business unit list").located_by("//ul[@id='select2-results-1']")
BTN_SAVE_UNIT = Target.the("button to save the list").located_by("//div[@class='tool-button save-and-close-button icon-tool-button']")
