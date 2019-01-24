from selenium.webdriver.common.by import By

# display_page
display_text_show = By.XPATH, "//*[contains(@text, '显示')]"
display_text_search = By.ID, 'com.android.settings:id/search'
display_input_edit_contnet = By.ID, 'android:id/search_src_text'
display_btn_back = By.CLASS_NAME, 'android.widget.ImageButton'

# appPackage/activity
# settings
app_settings = 'com.android.settings'
app_settings_activity = '.Settings'
# sms
app_sms = 'com.android.mms'
app_sms_activity = '.ui.ConversationList'


# network_page
network_text_more = By.XPATH, "//*[contains(@text, '更多')]"
network_text_mobile_net = By.XPATH, "//*[contains(@text, '移动网络')]"
network_text_first_network = By.XPATH, "//*[contains(@text, '首选网络')]"
network_2G = By.XPATH, "//*[contains(@text, '2G')]"
network_3G = By.XPATH, "//*[contains(@text, '3G')]"



# sms_page
new_add = By.ID, 'com.android.mms:id/action_compose_new'
sms_edit = By.ID, 'com.android.mms:id/recipients_editor'
input_sms_content = By.ID, "com.android.mms:id/embedded_text_editor"
sms_send_btn = By.ID, "com.android.mms:id/send_button_sms"
sms_send_lists = By.ID, "com.android.mms:id/text_view"


# setting_page
search_btn = By.ID, 'com.android.settings:id/search'

search_input = By.ID, 'android:id/search_src_text'

search_back_btn = By.CLASS_NAME, 'android.widget.ImageButton'