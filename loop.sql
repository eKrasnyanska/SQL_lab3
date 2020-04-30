DECLARE
    TYPE t_company IS VARRAY(5) OF company.company_name%TYPE;
    TYPE t_country IS VARRAY(5) OF company.country_c_code%TYPE;
    v_company t_company;
    v_country t_country;
BEGIN
    v_company := t_company('HBO Films', 'Warner Bros.', 'Lorimar Productions');
    v_country := t_country('USA', 'UK', 'USA');
    FOR i IN 1 .. v_company.count
    LOOP
        INSERT INTO company (company_name, country_c_code) VALUES (v_company(i), v_country(i));
        COMMIT;
    END LOOP;
END;