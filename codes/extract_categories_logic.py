def extract_categories(breadcrumbs_json):
    category_names = [""] * 4
    category_urls = [""] * 4
    try:
        breadcrumbs = eval(breadcrumbs_json)
        if isinstance(breadcrumbs, list):
            for idx, breadcrumb in enumerate(breadcrumbs[:4]):
                if isinstance(breadcrumb, dict):
                    category_names[idx] = breadcrumb.get("name", "")
                    category_urls[idx] = breadcrumb.get("url", "")
    except (NameError, TypeError, SyntaxError):
        print(f"Warning: Could not parse breadcrumbs JSON: {breadcrumbs_json}")
    return category_names, category_urls