package com.example.restexaple;


import android.app.ProgressDialog;
import android.content.Context;
import android.widget.Toast;

import com.loopj.android.http.AsyncHttpClient;
import com.loopj.android.http.JsonHttpResponseHandler;
import com.loopj.android.http.RequestParams;

import org.apache.http.Header;
import org.json.JSONException;
import org.json.JSONObject;

import java.lang.reflect.Method;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
/**
 * Class which has Utility methods
 *
 */


public class Utility {
    private static Pattern pattern;
    private static Matcher matcher;

    //Email Pattern
    private static final String EMAIL_PATTERN =
            "^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@"
                    + "[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$";

    /**
     * Validate Email with regular expression
     *
     * @param email
     * @return true for Valid Email and false for Invalid Email
     */
    public static boolean validate(String email) {
        pattern = Pattern.compile(EMAIL_PATTERN);
        matcher = pattern.matcher(email);
        return matcher.matches();

    }
    /**
     * Checks for Null String object
     *
     * @param txt
     * @return true for not null and false for null String object
     */
    public static boolean isNotNull(String txt){
        return txt!=null && txt.trim().length()>0 ? true: false;
    }


    static class Resposta {
        private int statusCode;
        private Header[] headers;
        private JSONObject responseJSON;
        private String responseString;
        private Throwable throwable;

        Resposta(int statusCode, Header[] headers, JSONObject responseJSON, String responseString) {
            this.statusCode = statusCode;
            this.headers = headers;
            this.responseJSON = responseJSON;
            this.responseString = responseString;
        }

        Resposta(int statusCode, Header[] headers, String responseString) {
            this.statusCode = statusCode;
            this.headers = headers;
            this.responseString = responseString;
            this.responseJSON = new JSONObject();
        }

        Resposta(int statusCode, Header[] headers, JSONObject responseJSON) {
            this.statusCode = statusCode;
            this.headers = headers;
            this.responseJSON = responseJSON;
            this.responseString = "";
        }

        public int getStatusCode() {
            return statusCode;
        }

        public void setStatusCode(int statusCode) {
            this.statusCode = statusCode;
        }

        public Header[] getHeaders() {
            return headers;
        }

        public void setHeaders(Header[] headers) {
            this.headers = headers;
        }

        public JSONObject getResponseJSON() {
            return responseJSON;
        }

        public void setResponseJSON(JSONObject responseJSON) {
            this.responseJSON = responseJSON;
        }

        public String getResponseString() {
            return responseString;
        }

        public void setResponseString(String responseString) {
            this.responseString = responseString;
        }
    }


    static public void tratarOnFailure(Resposta resposta, Context context) {
        String response;

        try {
            if (resposta.getStatusCode() == 0) {
                Toast.makeText(context, "Não foi possível conectar com o servidor. Verifique sua conexão com a interet", Toast.LENGTH_LONG).show();
            } else {
                if (resposta.getResponseString().equals("")) {
                    response = resposta.getResponseJSON().toString();
                } else {
                    response = resposta.getResponseString();
                }

                if (resposta.statusCode == 404) {
                    Toast.makeText(context, "Requested resource not found - 404 - " + response, Toast.LENGTH_LONG).show();
                }
                else if (resposta.statusCode == 500) {
                    Toast.makeText(context, "Something went wrong at server end - 500 - " + response, Toast.LENGTH_LONG).show();
                }
                else if (resposta.statusCode == 400) {
                    Toast.makeText(context, response.toString(), Toast.LENGTH_LONG).show();
                }
                else {
                    Toast.makeText(context, "Unexpected Error occured! " + Integer.toString(resposta.statusCode) + " - " + response, Toast.LENGTH_LONG).show();
                }
            }

        } catch(Exception e) {
            Toast.makeText(context, "Unexpected Error occured! " + e, Toast.LENGTH_LONG).show();
        }

    }

}