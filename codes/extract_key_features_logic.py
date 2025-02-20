def extract_key_features(key_features_json, summary_text):
    key_feature_list = []
    try:
        features = eval(key_features_json)
        if isinstance(features, list):
            key_feature_list = [feature.get("keyfeatures", "") for feature in features if isinstance(feature, dict)]
    except (NameError, TypeError, SyntaxError):
        print(f"Warning: Could not parse key features JSON: {key_features_json}")

    if not key_feature_list and summary_text:
        sentences = summary_text.split('.')
        key_feature_list = [s.strip() for s in sentences if s.strip()][:3]

    key_feature_1 = key_feature_list[0] if len(key_feature_list) > 0 else ""
    key_feature_2 = key_feature_list[1] if len(key_feature_list) > 1 else ""
    remaining_key_features = ". ".join(key_feature_list[2:]) if len(key_feature_list) > 2 else ""

    return key_feature_1, key_feature_2, remaining_key_features