package com.example.parkongo

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.fragment.app.Fragment
import com.example.parkongo.databinding.ActivityDashboardBinding

class dashboard : AppCompatActivity() {

    lateinit var binding: ActivityDashboardBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding=ActivityDashboardBinding.inflate(layoutInflater)
        val view=binding.root
        setContentView(view)
        supportActionBar?.hide()
        replacefragment(near_me())

        binding.bottomNavigationView.setOnItemSelectedListener {

            when(it.itemId){
                R.id.nearme -> replacefragment(near_me())
                R.id.reservation -> replacefragment(reservation())
                R.id.profile -> replacefragment(profile())
                R.id.Settings -> replacefragment(settings())
                else->{
                }
            }
            true


        }
    }

    private fun replacefragment(fragment:Fragment){
        val fragmentManager = supportFragmentManager
        val fragmentTransaction= fragmentManager.beginTransaction()
        fragmentTransaction.replace(R.id.frameLayout,fragment)
        fragmentTransaction.commit()
    }
}