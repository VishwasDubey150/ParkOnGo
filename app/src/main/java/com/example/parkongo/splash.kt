package com.example.parkongo

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Handler
import android.view.View
import android.view.animation.AnimationUtils
import androidx.core.view.isInvisible
import com.example.parkongo.databinding.ActivitySplashBinding

class splash : AppCompatActivity() {
    private lateinit var binding: ActivitySplashBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivitySplashBinding.inflate(layoutInflater) // Replace with your generated binding class name
        val view = binding.root
        setContentView(view)
        supportActionBar?.hide()
        binding.fadetv.visibility=View.INVISIBLE
        Handler().postDelayed({
            val mainIntent = Intent(this@splash, MainActivity::class.java)
            startActivity(mainIntent)
            finish()
        }, 3000)
    }

    override fun onStart() {
        super.onStart()
        Handler().postDelayed({
            val animation=AnimationUtils.loadAnimation(this,R.anim.fade_in)
            binding.fadetv.startAnimation(animation)
        }, 2200)
    }
}