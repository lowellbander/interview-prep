public ArrayList<String> merge (String[] a, String [] b) {
    ArrayList<String> sentence = new ArrayList<String>();
    for (String s : a) sentence.add(s);
    for (String s : b) sentence.add(s);
    return sentence;
}
