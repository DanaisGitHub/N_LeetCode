using System;
using NeetCodeC_;
// See https://aka.ms/new-console-template for more information

//class Output {
//    public static void NormalOutput(object val) {
//        Console.WriteLine(val);
//    }
//    public static void forEachOutput(IEnumerable<object> val) {
//        foreach (var x in val) {
//            Console.Write($"{val}, ");
//        }
//    }
//}
while (true) {
    string search = Console.ReadLine()!;

    var val = BinarySearch.SearchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], int.Parse(search!));

    Console.WriteLine(val);
}
//foreach (var x in val) {
//    Console.WriteLine(x);
//}

//Console.WriteLine(string.Join(', ',Arrays.GroupAnagrams(['act', 'pots', 'tops', 'cat', 'stop', 'hat'])));
Console.ReadLine();


