package com.example.parkongo

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import androidx.core.view.ViewCompat
import com.example.parkongo.databinding.ActivityLogin2Binding

class login : AppCompatActivity() {
    lateinit var binding: ActivityLogin2Binding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding=ActivityLogin2Binding.inflate(layoutInflater)
        val view = binding.root
        setContentView(view)
        supportActionBar?.hide()

    }

    fun dash(view: View) {
        val mainIntent = Intent(this@login,dashboard::class.java)
        startActivity(mainIntent)
    }
}