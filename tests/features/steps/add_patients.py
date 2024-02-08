from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@when(u'I click on Patient menu')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[text()='Patient']").click()


@when(u'I click on New Search menu')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[text()='New/Search']").click()


@when(u'I fill the patient details form')
def step_impl(context):
    context.driver.switch_to.frame(context.driver.find_element(By.XPATH,"//iframe[@name='pat']"))
    context.driver.find_element(By.ID, "form_fname").send_keys(context.table.rows[0]["firstname"])
    context.driver.find_element(By.CSS_SELECTOR, "#form_lname").send_keys(context.table.rows[0]["lastname"])
    # print(len(context.table.rows))
    context.driver.find_element(By.NAME, "form_DOB").send_keys(context.table.rows[0]["dob"])
    pat_gender = Select(context.driver.find_element(By.XPATH, "//select[@name='form_sex']"))
    pat_gender.select_by_visible_text(context.table.rows[0]['gender'])
    #push code to github


@when(u'I click on create new patient')
def step_impl(context):
    print("hi")


@when(u'I click on confirm create new patient')
def step_impl(context):
    print("hi")


@when(u'I handle the alert box')
def step_impl(context):
    print("hi")


@when(u'I close the birthday popup if available')
def step_impl(context):
    print("hi")


@then(u'I should get the added patient record as "{expected_patient_name}"')
def step_impl(context,expected_patient_name):
    print(expected_patient_name)