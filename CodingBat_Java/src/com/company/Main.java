package com.company;

import java.util.HashMap;
import java.util.Map;

public class Main {

    public static void main(String[] args) {
	// write your code here

        //multiple addition of key-value pair for map
        Map_1 map_1 = new Map_1();
        Map<String,String> map = new HashMap<String, String>()
        {{
            put("a","aaa");
            put("b","bbb");
            put("c","ccc");

        }};
        System.out.println(map_1.mapShare(map));

        // multiple addition of string on array
        Map_2 map_2 = new Map_2();
        String[] data = new String[]{"a", "b", "a", "c", "a", "d", "a"};
        System.out.println(map_2.wordAppend(data));


        Strings_1 strings_1 = new Strings_1();
        System.out.println(strings_1.twoChar("java", 4) );

        Warmup_2 warmup_2 = new Warmup_2();
        System.out.println(warmup_2.stringMatch("aabbccdd", "abbbxxd"));


    }


}
