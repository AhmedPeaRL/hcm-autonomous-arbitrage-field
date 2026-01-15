def execute(action, context):
    if not context["right_of_action"]:
        return "DENIED"

    if context["already_executed"]:
        return "SILENT_EXIT"

    # تنفيذ الفعل مرة واحدة فقط
    result = action()
    return result
