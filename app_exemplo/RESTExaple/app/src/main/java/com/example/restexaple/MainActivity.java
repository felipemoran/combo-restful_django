package com.example.restexaple;

import android.app.ProgressDialog;
import android.content.Context;
import android.content.SharedPreferences;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import com.loopj.android.http.AsyncHttpClient;
import com.loopj.android.http.JsonHttpResponseHandler;
import com.loopj.android.http.RequestParams;

import org.apache.http.Header;
import org.apache.http.message.BasicHeader;
import org.json.JSONException;
import org.json.JSONObject;



public class MainActivity extends ActionBarActivity {
    // Progress Dialog Object
    ProgressDialog prgDialog;

    SharedPreferences loginInfo;
    SharedPreferences.Editor loginInfoEditor;

    Button ButtonAuthGet;
    Button ButtonAuthPost;
    Button ButtonUnauthGet;
    Button ButtonUnauthPost;

    String URL = "http://192.168.1.226:8000/teste";
    String url;
    String prgDialogText;

    Context context;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        context = this;

        loginInfo = getSharedPreferences("loginInfo", 0);
        loginInfoEditor = loginInfo.edit();

        ButtonAuthGet = (Button) findViewById(R.id.auth_get);
        ButtonAuthPost = (Button) findViewById(R.id.auth_post);
        ButtonUnauthGet = (Button) findViewById(R.id.unauth_get);
        ButtonUnauthPost = (Button) findViewById(R.id.unauth_post);

        // Instancia a caixa de progresso
        prgDialog = new ProgressDialog(this);
        // Defini qual é a mensagem da caixa de prograsso
        prgDialog.setMessage("Loading info...");
        // Faz com que não seja cancelável
        prgDialog.setCancelable(false);

        prgDialogText = "Carregando informações... ";


        ButtonAuthGet.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Header[] headers = {
                        new BasicHeader("Authorization", "Token " + loginInfo.getString("auth_token", "0"))
                };

                RequestParams params = new RequestParams();
                if (!params.equals("0")) {
                    params.put("chave", "valor");
                }

                // Chamadas GET não podem ter a '/' no final
                url = URL;

                invokeWSGet(params, headers, url);

            }
        });


        ButtonAuthPost.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Header[] headers = {
                        new BasicHeader("Authorization", "Token " + loginInfo.getString("auth_token", "0"))
                };

                RequestParams params = new RequestParams();
                if (!params.equals("0")) {
                    params.put("chave", "valor");
                }

                // Chamadas POST devem ter a '/' no final
                url = URL + '/';

                invokeWSPost(params, headers, url);
            }
        });

        ButtonUnauthGet.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Header[] headers = {};

                RequestParams params = new RequestParams();
                if (!params.equals("0")) {
                    params.put("chave", "valor");
                }

                // Chamadas GET não podem ter a '/' no final
                url = URL;

                invokeWSGet(params, headers, url);
            }
        });

        ButtonUnauthPost.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Header[] headers = {};

                RequestParams params = new RequestParams();
                if (!params.equals("0")) {
                    params.put("chave", "valor");
                }

                // Chamadas POST devem ter a '/' no final
                url = URL + '/';

                invokeWSPost(params, headers, url);
            }
        });


    }


    public void invokeWSGet(RequestParams params, org.apache.http.Header[] headers, String url){
        // Mostra a caixa de progresso
        prgDialog.show();

        // Faz uma chamada ao Django usando um objeto AsyncHttpClient
        AsyncHttpClient client = new AsyncHttpClient();
        client.get(this, url, headers, params, new JsonHttpResponseHandler() {


            // Entra quando a resposta foi OK, código 200
            @Override
            public void onSuccess(int statusCode, Header[] headers, JSONObject response) {
                // Hide Progress Dialog
                prgDialog.hide();
                Utility.Resposta resposta = new Utility.Resposta(statusCode, headers, response);
                tratarOnSuccess(resposta, context);
            }


            // Quando acontece algum erro essas funcoes sao chamadas (statusCude != 200)

            // Essa funcao é chamada quando a resposta do erro vem em forma de texto (ex.: pagina amarela do django)
            @Override
            public void onFailure(int statusCode, org.apache.http.Header[] headers, String response, java.lang.Throwable throwable) {
                prgDialog.hide();

                Utility.Resposta resposta = new Utility.Resposta(statusCode, headers, response);
                Utility.tratarOnFailure(resposta, context);

            }

            // Essa funcao é chamada quando a resposta do erro vem em forma de json (ex.: credenciais de acesso nao aceitas ou a propria views manda uma resposta em json com codigo de status diferente de 200)
            @Override
            public void onFailure(int statusCode, Header[] headers, java.lang.Throwable error, JSONObject response) {
                prgDialog.hide();

                Utility.Resposta resposta = new Utility.Resposta(statusCode, headers, response);
                Utility.tratarOnFailure(resposta, context);
            }
        });
    }


    public void invokeWSPost(RequestParams params, org.apache.http.Header[] headers, String url){
        prgDialog.show();
        AsyncHttpClient client = new AsyncHttpClient();
        client.post(this, url, headers, params, "application/json", new JsonHttpResponseHandler() {
            @Override
            public void onSuccess(int statusCode, org.apache.http.Header[] headers, JSONObject response) {
                prgDialog.hide();
                Utility.Resposta resposta = new Utility.Resposta(statusCode, headers, response);
                tratarOnSuccess(resposta, context);
            }
            @Override
            public void onFailure(int statusCode, org.apache.http.Header[] headers, String response, java.lang.Throwable throwable) {
                prgDialog.hide();
                Utility.Resposta resposta = new Utility.Resposta(statusCode, headers, response);
                Utility.tratarOnFailure(resposta, context);
            }
            @Override
            public void onFailure(int statusCode, Header[] headers, java.lang.Throwable error, JSONObject response) {
                prgDialog.hide();
                Utility.Resposta resposta = new Utility.Resposta(statusCode, headers, response);
                Utility.tratarOnFailure(resposta, context);
            }
        });
    }


    static public void tratarOnSuccess(Utility.Resposta resposta, Context context) {
        try {
            JSONObject obj = resposta.getResponseJSON();

            // Olha se o json tem o par chave-valor que esperamos como resposta
            if (obj.has("texto")) {
                Toast.makeText(context, obj.getString("texto"), Toast.LENGTH_SHORT).show();
            }
            // Avisa se não achar o par
            else {
                Toast.makeText(context, "JSON recebido não tem a chave texto -> " + obj, Toast.LENGTH_SHORT).show();
            }
        } catch (JSONException e) {
            // TODO Auto-generated catch block
            Toast.makeText(context, "Error Occured [Bad JSON]! " + resposta.getResponseJSON(), Toast.LENGTH_SHORT).show();
            e.printStackTrace();

        }
    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_logout) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}
