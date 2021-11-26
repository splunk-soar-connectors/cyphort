# --
# File: cyphort_consts.py
#
# Copyright (c) 2014-2021 Splunk Inc.
#
# This unpublished material is proprietary to Phantom Cyber.
# All rights reserved. The methods and
# techniques described herein are considered trade secrets
# and/or confidential. Reproduction or distribution, in whole
# or in part, is forbidden except by express written permission
# of Phantom Cyber.
#
# --

CYPHORT_ERR_CONNECTIVITY_TEST = "Connectivity test failed"
CYPHORT_SUCC_CONNECTIVITY_TEST = "Connectivity test passed"
CYPHORT_ERR_SERVER_CONNECTION = "Connection failed"
CYPHORT_ERR_FROM_SERVER = "API failed, Status Code: {status_code}, Status: {status}, Message: {message}"
CYPHORT_USING_BASE_URL = "Using url: {base_url}"
CYPHORT_MSG_QUERYING_USERS_CHECK_CREDS = "Querying users to check for credentials"
CYPHORT_MSG_FILE_SUBMITTED = "Submitted file"
CYPHORT_MSG_POLL_TRY = "Polling attempt {0}. Analysis pending"
CYPHORT_MSG_ANALYSIS_COMPLETE = "Analysis complete, getting results"

CYPHORT_REST_API_URL = "https://{server}/cyadmin/api.php"
CYPHORT_REST_API_UPLOAD_FILE_URL = "https://{server}/cyadmin/cgi-bin/file_submit"
CYPHORT_JSON_APIKEY = "api_key"  # pragma: allowlist secret
CYPHORT_JSON_SERVER = "server"
CYPHORT_JSON_ID = "id"
CYPHORT_JSON_ANALYSIS = "analysis_details"
CYPHORT_JSON_BEHAVIOR = "behavior_details"
CYPHORT_JSON_EVENT_ID = "event_id"
CYPHORT_JSON_TARGET = "target"

CYPHORT_SUCC_ANALYSIS_INCOMPLETE = "Reached max polling attempts. Please use the <b>event_id</b>" \
                                   " as a parameter to <b>get report</b> to query the report status."
CYPHORT_POLL_SLEEP_SECS = 10
CYPHORT_MAX_POLL_TIMES = 20
