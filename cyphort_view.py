# --
# File: cyphort_view.py
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


def get_ctx_result(result):

    ctx_result = {}
    param = result.get_param()

    ctx_result['task_id'] = param.get('id')
    ctx_result['vault_id'] = param.get('vault_id')
    ctx_result['vault_file_name'] = param.get('file_name')

    data = result.get_data()

    if (not data):
        return ctx_result

    data = data[0]

    if (not data):
        return ctx_result

    ctx_result['analysis_details'] = data.get('analysis_details', {}).get('analysis_details')
    ctx_result['analysis_array'] = data.get('analysis_details', {}).get('analysis_array')
    ctx_result['behavior_details'] = data.get('behavior_details')

    message = result.get_message()

    if (message) and ('max polling attempts' in message):
        ctx_result['message'] = message

    return ctx_result


def display_report(provides, all_app_runs, context):

    context['results'] = results = []
    for summary, action_results in all_app_runs:
        for result in action_results:

            ctx_result = get_ctx_result(result)
            if (not ctx_result):
                continue
            results.append(ctx_result)
    # print context
    return 'cyphort_display_report.html'
