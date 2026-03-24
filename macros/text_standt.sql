{% macro standardize_text(column_name) %}
    lower(trim(regexp_replace({{ column_name }}, '\s+', ' ', 'g')))
{% endmacro %}