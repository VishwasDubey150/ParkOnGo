package com.example.parkongo

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        supportActionBar?.hide()
    }

    fun login(view: View) {
        val mainIntent = Intent(this@MainActivity, login::class.java)
        startActivity(mainIntent)
        finish()
    }
}