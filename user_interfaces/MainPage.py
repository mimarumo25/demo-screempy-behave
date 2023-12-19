from screenpy_selenium import Target


THE_DASHBOARD_TITLE = Target.the("Dashboard Title").located_by("//h1[contains(text(),'Dashboard')]")
BTN_ORGANIZATION = Target.the("button organization").located_by("//i[@class='s-sidebar-icon fa fa-sitemap premium-feature']")
BTN_BUSINESS_UNIT = Target.the("business name field").located_by("//i[@class='s-sidebar-icon fa fa-sitemap']")
BTN_NEW_BUSINESS = Target.the("button to select businessUnit").located_by("//div[@class='tool-button add-button icon-tool-button']")

